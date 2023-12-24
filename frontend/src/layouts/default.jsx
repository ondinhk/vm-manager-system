import { Container, Nav, Navbar } from 'react-bootstrap'
import { Outlet, Link } from 'react-router-dom'

const Layout = () => {
    return (
        <>
            <Navbar bg='dark' data-bs-theme='dark'>
                <Container>
                    <Navbar.Brand as={Link} to='/'>
                        Mange VMs System
                    </Navbar.Brand>
                    <Nav className='me-auto'>
                        <Nav.Link as={Link} to='/'>
                            Manage VMs
                        </Nav.Link>
                        <Nav.Link as={Link} to='/manage-action'>
                            Manage Actions
                        </Nav.Link>
                        <Nav.Link as={Link} to='/manage-video'>
                            Manage Videos
                        </Nav.Link>
                        <Nav.Link as={Link} to='/rdp-views'>
                            VMs Views
                        </Nav.Link>
                    </Nav>
                </Container>
            </Navbar>
            <content className='container'>
                <Outlet />
            </content>
        </>
    )
}

export default Layout
