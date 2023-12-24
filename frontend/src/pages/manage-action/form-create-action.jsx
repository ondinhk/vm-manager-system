import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import * as formik from 'formik'
import * as yup from 'yup'
import { CONSTANTS } from 'utils/constants'
import { InputGroup } from 'react-bootstrap'

function FormAction({ fetchData, show, handleClose }) {
    const { Formik } = formik

    const schema = yup.object().shape({
        vm_name: yup.string().required(),
        username: yup.string().required(),
        password: yup.string().required(),
        email: yup.string().required(),
        email_password: yup.string().required(),
    })

    const handleCreateAction = async (progs) => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/actions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(progs),
            })
                .then((data) => data.json())
                .then((data) => {
                    let text = data.detail === undefined ? data : data.detail
                    alert(text)
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
                // validationSchema={schema}
                onSubmit={async (value, { resetForm }) => {
                    resetForm()
                    await handleCreateAction(value)
                }}
                initialValues={{
                    vm_name: '',
                    username: '',
                    password: '',
                    email: '',
                    email_password: '',
                    platform: 'like4like',
                    channel: 'youtube',
                }}
            >
                {({ handleSubmit, handleChange, values, touched, errors }) => (
                    <Modal show={show} onHide={handleClose}>
                        <Modal.Header closeButton>
                            <Modal.Title>Create Action</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            <Form noValidate onSubmit={handleSubmit}>
                                <Row className='mb-3'>
                                    <Form.Group as={Col} md='6' controlId='validationFormik01'>
                                        <Form.Label>VM name:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='vm_name'
                                            value={values.vm_name}
                                            onChange={handleChange}
                                            isValid={touched.vm_name && !errors.vm_name}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='6' controlId='validationFormik01'>
                                        <Form.Label>Username:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='username'
                                            value={values.username}
                                            onChange={handleChange}
                                            isValid={touched.username && !errors.username}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                </Row>
                                <Row className='mb-3'>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Password:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='password'
                                            value={values.password}
                                            onChange={handleChange}
                                            isValid={touched.password && !errors.password}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Platform:</Form.Label>
                                        <Form.Control
                                            as='select'
                                            name='platform'
                                            value={values.platform}
                                            onChange={handleChange}
                                            isValid={touched.platform && !errors.platform}
                                        >
                                            <option value='like4like' label='Like4Like' />
                                            <option value='view' label='View' />
                                        </Form.Control>
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Channel:</Form.Label>
                                        <Form.Control
                                            as='select'
                                            name='channel'
                                            value={values.channel}
                                            onChange={handleChange}
                                            isValid={touched.channel && !errors.channel}
                                        >
                                            <option value='youtube' label='Youtube' />
                                            <option value='tiktok' label='Tiktok' />
                                        </Form.Control>
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                </Row>
                                <Row>
                                    <Form.Label>Email:</Form.Label>
                                    <InputGroup hasValidation>
                                        <Form.Control
                                            type='text'
                                            aria-describedby='inputGroupPrepend'
                                            name='email'
                                            value={values.email}
                                            onChange={handleChange}
                                            isInvalid={!!errors.email}
                                        />
                                        <Form.Control.Feedback type='invalid'>{errors.email}</Form.Control.Feedback>
                                    </InputGroup>
                                </Row>
                                <Row>
                                    <Form.Label>Email Password:</Form.Label>
                                    <InputGroup hasValidation>
                                        <Form.Control
                                            type='text'
                                            aria-describedby='inputGroupPrepend'
                                            name='email_password'
                                            value={values.email_password}
                                            onChange={handleChange}
                                            isInvalid={!!errors.email_password}
                                        />
                                        <Form.Control.Feedback type='invalid'>
                                            {errors.email_password}
                                        </Form.Control.Feedback>
                                    </InputGroup>
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

export default FormAction
