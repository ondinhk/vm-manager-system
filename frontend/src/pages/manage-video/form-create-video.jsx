import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import * as formik from 'formik'
import * as yup from 'yup'
import { CONSTANTS } from 'utils/constants'

function FormVideo({ fetchData, show, handleClose }) {
    const { Formik } = formik

    const schema = yup.object().shape({
        video_name: yup.string().required(),
        video_time: yup.string().required(),
    })

    const handleCreateVideo = async (progs) => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/videos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(progs),
            })
                .then((data) => data.json())
                .then((data) => {
                    alert(data)
                    handleClose()
                })
            await fetchData()
        } catch (error) {
            alert('Create error', error)
        }
    }

    return (
        <>
            <Formik
                validationSchema={schema}
                onSubmit={async (value, { resetForm }) => {
                    resetForm()
                    await handleCreateVideo(value)
                }}
                initialValues={{
                    video_name: '',
                    video_time: '',
                }}
            >
                {({ handleSubmit, handleChange, values, touched, errors }) => (
                    <Modal show={show} onHide={handleClose}>
                        <Modal.Header closeButton>
                            <Modal.Title>Create Video</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            <Form noValidate onSubmit={handleSubmit}>
                                <Row className='mb-3'>
                                    <Form.Group as={Col} md='8' controlId='validationFormik01'>
                                        <Form.Label>Video Name:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='video_name'
                                            value={values.video_name}
                                            onChange={handleChange}
                                            isValid={touched.video_name && !errors.video_name}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Video Time:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='video_time'
                                            value={values.video_time}
                                            onChange={handleChange}
                                            isValid={touched.video_time && !errors.video_time}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                </Row>
                                <Modal.Footer>
                                    <Button variant='secondary' onClick={handleClose}>
                                        Close
                                    </Button>
                                    <Button variant='primary' type='submit'>
                                        Create
                                    </Button>
                                </Modal.Footer>
                            </Form>
                        </Modal.Body>
                    </Modal>
                )}
            </Formik>
        </>
    )
}

export default FormVideo
