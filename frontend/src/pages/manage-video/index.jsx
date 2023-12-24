import { Button } from 'react-bootstrap'
import Table from 'react-bootstrap/Table'
import { useEffect, useState } from 'react'
import { CONSTANTS } from 'utils/constants'
import FormVideo from './form-create-video'

const ManageVideo = () => {
    const [data, setData] = useState([])
    const [show, setShow] = useState(false)
    const [error, setError] = useState(false)

    const handleClose = () => setShow(false)
    const handleShow = () => setShow(true)

    useEffect(() => {
        document.title = 'Manage Videos'
        fetchData()
    }, [])

    const fetchData = async () => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/videos')
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
                const api_delete = CONSTANTS['BASE_API'] + '/videos/' + id
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
                        <FormVideo fetchData={fetchData} handleClose={handleClose} show={show} />
                        <Button variant='success' onClick={handleShow} className='me-2'>
                            Add Video
                        </Button>
                        <Button variant='secondary' className='me-2' onClick={fetchData}>
                            Refresh Page {error ? 'Error' : ''}
                        </Button>
                    </div>
                </div>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Name</th>
                            <th>Time</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((row, index) => (
                            <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{row.video_name}</td>
                                <td>{row.video_name}</td>
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

export default ManageVideo
