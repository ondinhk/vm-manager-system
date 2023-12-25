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

    const openChrome = async () => {
        try {
            await fetch(CONSTANTS['BASE_API'] + '/vms/execute/chrome-open')
        } catch (error) { }
    }

    const loginChrome = async () => {
        try {
            await fetch(CONSTANTS['BASE_API'] + '/vms/execute/chrome-login')
        } catch (error) { }
    }

    const openYoutube = async () => {
        try {
            await fetch(CONSTANTS['BASE_API'] + '/vms/execute/chrome-youtube')
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
                    <Button variant='success' className='me-2' onClick={openChrome}>
                        Open Chrome
                    </Button>
                    <Button variant='secondary' className='me-2' onClick={loginChrome}>
                        Login Chrome
                    </Button>
                    <Button variant='danger' className='me-2' onClick={openYoutube}>
                        Open Youtube
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
                {/* <div>
                    <Button variant='success' className='me-2'>
                        Start
                    </Button>
                    <Button variant='danger' className='me-2'>
                        Stop
                    </Button>
                </div> */}
            </div>
            <div className={styles.container}>
                {data.map((vm, index) => (
                    <RDPView key={index} name={vm.name} url={vm.ip_address} />
                ))}
            </div>
        </>
    )
}

export default RDPManage
