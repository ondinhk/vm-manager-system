import ManageVideo from 'pages/manage-video'
import Layout from './layouts/default'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ManageVM from './pages/manage-vm'
import RDPViews from './pages/rdp-view'
import ManageAction from 'pages/manage-action'

function App() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<Layout />}>
                        <Route index element={<ManageVM />} />
                        <Route path='rdp-views' element={<RDPViews />} />
                        <Route path='manage-video' element={<ManageVideo />} />
                        <Route path='manage-action' element={<ManageAction />} />
                        {/* <Route path="*" element={<NoPage />} /> */}
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App
