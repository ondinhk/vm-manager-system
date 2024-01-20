import styles from './styles.module.css'
// import { VncScreen } from 'react-vnc';

const RDPView = ({ name, group, url }) => {
    return (
        <>
            <div className={styles.view}>
                {/* <VncScreen
                    url={url}
                    //scaleViewport
                    resizeSession
                    background="#000000"
                    rfbOptions={{
                        credentials: {
                            password: 'password'
                        }
                    }}
                    style={{
                        width: '900px',
                        height: '760px',
                    }}
                /> */}
                <iframe title="" width="900" height="760" src={url} frameBorder="0" />
                {name} {group}
            </div>
        </>
    )
}

export default RDPView
