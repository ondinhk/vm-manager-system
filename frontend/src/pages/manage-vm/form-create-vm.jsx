import { useEffect, useState } from 'react'
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'
import Row from 'react-bootstrap/Row'
import * as formik from 'formik'
import * as yup from 'yup'
import { CONSTANTS } from 'utils/constants'

function FormVM({ fetchDataVMs, show, handleClose }) {
    const { Formik } = formik

    const schema = yup.object().shape({
        name: yup.string().required(),
        ip_address: yup.string().required(),
        group: yup.string().required(),
    })

    const handleCreateVM = async (progs) => {
        try {
            const response = await fetch(CONSTANTS['BASE_API'] + '/vms', {
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
            await fetchDataVMs()
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
                    await handleCreateVM(value)
                }}
                initialValues={{
                    name: 'VM_',
                    ip_address: 'ws://',
                    proxy: '',
                    group: '',
                }}
            >
                {({ handleSubmit, handleChange, values, touched, errors }) => (
                    <Modal show={show} onHide={handleClose}>
                        <Modal.Header closeButton>
                            <Modal.Title>Create VM</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            <Form noValidate onSubmit={handleSubmit}>
                                <Row className='mb-3'>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Name VM:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='name'
                                            value={values.name}
                                            onChange={handleChange}
                                            isValid={touched.name && !errors.name}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='4' controlId='validationFormik01'>
                                        <Form.Label>Group VM:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            name='group'
                                            value={values.group}
                                            onChange={handleChange}
                                            isValid={touched.group && !errors.group}
                                        />
                                        <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                                    </Form.Group>
                                </Row>
                                <Row className='mb-3'>
                                    <Form.Group as={Col} md='6' controlId='validationFormik03'>
                                        <Form.Label>IP:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            placeholder='IP address'
                                            name='ip_address'
                                            value={values.ip_address}
                                            onChange={handleChange}
                                            isInvalid={!!errors.ip_address}
                                        />
                                        <Form.Control.Feedback type='invalid'>
                                            {errors.ip_address}
                                        </Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group as={Col} md='6' controlId='validationFormik05'>
                                        <Form.Label>Proxy:</Form.Label>
                                        <Form.Control
                                            type='text'
                                            placeholder='Proxy'
                                            name='proxy'
                                            value={values.proxy}
                                            onChange={handleChange}
                                            isInvalid={!!errors.proxy}
                                        />

                                        <Form.Control.Feedback type='invalid'>{errors.proxy}</Form.Control.Feedback>
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

export default FormVM
