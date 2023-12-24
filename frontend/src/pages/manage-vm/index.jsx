import { Button } from 'react-bootstrap'
import Table from 'react-bootstrap/Table'
import { useEffect, useState } from 'react'
import { CONSTANTS } from 'utils/constants'
import FormVM from './form-create-vm'

const ManageVM = () => {
    const [data, setData] = useState([])
    const [filterGroup, setFilterGroup] = useState('')
    const [show, setShow] = useState(false)
    const [error, setError] = useState(false)

    const handleClose = () => setShow(false)
    const handleShow = () => setShow(true)

    useEffect(() => {
        document.title = 'Manage VMs'
        fetchDataVMs()
    }, [])

    const fetchDataVMs = async () => {
        try {
            console.log(CONSTANTS['BASE_API'] + '/vms')
            const response = await fetch(CONSTANTS['BASE_API'] + '/vms')
            const result = await response.json()
            setData(result)
            setError(false)
        } catch (error) {
            setData([])
            setError(true)
        }
    }

    const filteredData = data.filter((row) => row.group.toLowerCase().includes(filterGroup.toLowerCase()))

    const handleFilterChange = (event) => {
        setFilterGroup(event.target.value)
    }

    const deleteVM = async (id) => {
        try {
            if (window.confirm('Are you sure to delete this VM')) {
                const api_delete = CONSTANTS['BASE_API'] + '/vms/' + id
                await fetch(api_delete, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                })
                alert('Delete success')
                await fetchDataVMs()
            }
        } catch (error) {
            alert('Delete erorr ', error)
        }
    }

    return (
        <>
            <div className='container-fluid'>
                <div className='mb-4 d-flex justify-content-between align-items-center'>
                    <div className='d-flex align-items-center'>
                        <FormVM fetchDataVMs={fetchDataVMs} handleClose={handleClose} show={show} />
                        <Button variant='success' onClick={handleShow} className='me-2'>
                            Add VM
                        </Button>
                        <Button variant='secondary' className='me-2' onClick={fetchDataVMs}>
                            Refresh Page {error ? 'Error' : ''}
                        </Button>
                    </div>
                    <div className='me-2'>
                        <input
                            type='text'
                            placeholder='Filter by Group'
                            value={filterGroup}
                            onChange={handleFilterChange}
                        />
                    </div>
                </div>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Group</th>
                            <th>Name</th>
                            <th>IP Adress</th>
                            <th>Proxy</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredData.map((row, index) => (
                            <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{row.group}</td>
                                <td>{row.name}</td>
                                <td>{row.ip_address}</td>
                                <td>{row.proxy}</td>
                                <td>
                                    <div>
                                        <Button variant='danger' className='me-2' onClick={() => deleteVM(row.id)}>
                                            Delete
                                        </Button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
        </>
    )
}

export default ManageVM
