import { Button } from 'react-bootstrap'
import Table from 'react-bootstrap/Table'
import { useEffect, useState } from 'react'
import { CONSTANTS } from 'utils/constants'
import FormAction from './form-create-action'

const actionList = ['like4like', 'followlike', 'view']
const typeList = ['youtube', 'tiktok']
const statusList = ['200', '500']

const ManageAction = () => {
    const [data, setData] = useState([])
    const [show, setShow] = useState(false)
    const [error, setError] = useState(false)

    const handleClose = () => setShow(false)
    const handleShow = () => setShow(true)

    const [selectedAction, setSelectedAction] = useState('')
    const [selectedType, setSelectedType] = useState('')
    const [selectedStatus, setSelectedStatus] = useState('')

    const handleActionChange = (event) => {
        setSelectedAction(event.target.value)
    }
    const handleTypeChange = (event) => {
        setSelectedType(event.target.value)
    }
    const handleTypeStatus = (event) => {
        setSelectedStatus(event.target.value)
    }

    const updateActions = async () => {
        if (selectedAction !== '' || selectedType !== '') {
            if (window.confirm('Are you sure to sync action?')) {
                data.forEach(async (item) => {
                    item['platform'] = selectedAction
                    item['channel'] = selectedType
                    item['status'] = selectedStatus
                    await handleUpdateAction(item.id, item)
                    await fetchData()
                })
            }
        } else {
            alert('Please sellect action')
        }
    }

    const handleUpdateAction = async (id, data) => {
        try {
            const api = CONSTANTS['BASE_API'] + '/actions/' + id
            const response = await fetch(api, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            })
            if (!response.ok) {
                throw new Error(`Error updating action for ID ${id}: ${response.statusText}`)
            }
        } catch (error) {
            alert(`Sync error ${error}`)
        }
    }

    useEffect(() => {
        document.title = 'Manage Action'
        fetchData()
    }, [])

    const fetchData = async () => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/actions')
            const result = await response.json()
            setData(result)
        } catch (error) {
            setData([])
            setError(true)
        }
    }

    const deleteVM = async (id) => {
        try {
            if (window.confirm('Are you sure to delete this VM')) {
                const api_delete = CONSTANTS['BASE_API'] + '/actions/' + id
                await fetch(api_delete, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                })
                alert('Delete success')
                await fetchData()
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
                        <FormAction fetchData={fetchData} handleClose={handleClose} show={show} />
                        <Button variant='success' onClick={handleShow} className='me-2'>
                            Add Action
                        </Button>
                        <Button variant='secondary' className='me-2' onClick={fetchData}>
                            Refresh Page {error ? 'Error' : ''}
                        </Button>
                    </div>
                    <div className='me-2'>
                        <Button variant='warning' className='me-2' onClick={updateActions}>
                            Sync actions
                        </Button>
                        <select
                            className='me-2'
                            name='actions'
                            id='actions'
                            value={selectedAction}
                            onChange={handleActionChange}
                        >
                            <option value=''>Action</option>
                            {actionList.map((action, index) => (
                                <option key={index} value={action}>
                                    {action}
                                </option>
                            ))}
                        </select>
                        <select
                            className='me-2'
                            name='types'
                            id='types'
                            value={selectedType}
                            onChange={handleTypeChange}
                        >
                            <option value=''>Type</option>
                            {typeList.map((action, index) => (
                                <option key={index} value={action}>
                                    {action}
                                </option>
                            ))}
                        </select>
                        <select
                            className='me-2'
                            name='status'
                            id='status'
                            value={selectedStatus}
                            onChange={handleTypeStatus}
                        >
                            <option value=''>Status</option>
                            {statusList.map((action, index) => (
                                <option key={index} value={action}>
                                    {action}
                                </option>
                            ))}
                        </select>
                    </div>
                </div>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>VM name</th>
                            <th>Email</th>
                            <th>Email Password</th>
                            <th>Username</th>
                            <th>Password</th>
                            <th>Platform</th>
                            <th>Channel</th>
                            <th>Status</th>
                            <th>Alive</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((row, index) => (
                            <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{row.vm_name}</td>
                                <td>{row.email}</td>
                                <td>{row.email_password}</td>
                                <td>{row.username}</td>
                                <td>{row.password}</td>
                                <td>{row.platform}</td>
                                <td>{row.channel}</td>
                                <td>
                                    {row.status === 200 ? (
                                        <p className='text-success'>Running</p>
                                    ) : (
                                        <p className='text-danger'>Stopped</p>
                                    )}
                                </td>
                                <td>{row.alive}</td>
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

export default ManageAction
