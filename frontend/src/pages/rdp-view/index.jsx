import RDPView from 'components/rdp/RDPView'
import styles from './styles.module.css'
import { useEffect, useState } from 'react'
import { CONSTANTS } from 'utils/constants'
import { Button } from 'react-bootstrap'

const RDPManage = () => {
    const [data, setData] = useState([])
    const [inputValue, setInputValue] = useState('')

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const fetchDataVMs = async () => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/vms')
            const result = await response.json()
            setData(result)
        } catch (error) {
            alert('Error to fetch data', error)
        }
    }

    const sendAction = async (action) => {
        try {
            await fetch(CONSTANTS['BASE_API'] + '/vms/execute/' + action)
        } catch (error) { }
    }

    const sendClipboard = async () => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/vms/execute/input', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'input_value': inputValue }),
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
        } catch (error) { }
    }

    useEffect(() => {
        document.title = 'View RDPs'
        fetchDataVMs()
    }, [])

    return (
        <>
            <div className='mb-2 d-flex justify-content-around align-items-center'>
                <div className='d-flex align-items-center'>
                    <Button variant='info' className='me-2' onClick={fetchDataVMs}>
                        Refresh
                    </Button>
                    <Button variant='success' className='me-2' onClick={() => sendAction('chrome-open')}>
                        Open Chrome
                    </Button>
                    <Button variant='danger' className='me-2' onClick={() => sendAction('chrome-proxy')}>
                        Open Proxy
                    </Button>
                    <Button variant='info' className='me-2' onClick={() => sendAction('chrome-proxy-refresh')}>
                        Stop Proxy
                    </Button>
                    <Button variant='info' className='me-2' onClick={() => sendAction('chrome-actions')}>
                        Actions
                    </Button>
                    <Button variant='info' className='me-2' onClick={() => sendAction('chrome-close')}>
                        Close
                    </Button>
                </div>
                <div className='d-flex align-items-center'>
                    <input
                        type="text"
                        value={inputValue}
                        onChange={handleInputChange}
                    />
                    <Button variant='info' className='me-2' onClick={sendClipboard}>
                        Send Clipboard
                    </Button>
                </div>
                <div>
                    <h3>Active worker: {data.length}</h3>
                </div>
            </div>
            <div className={styles.container}>
                {data.map((vm, index) => (
                    <RDPView key={index} name={vm.name} url={vm.ip_address} group={vm.group} />
                ))}
            </div>
        </>
    )
}

export default RDPManage
