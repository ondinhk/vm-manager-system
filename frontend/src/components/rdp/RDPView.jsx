import styles from './styles.module.css'
import { VncScreen } from 'react-vnc';

const RDPView = ({ name, group, url }) => {
    return (
        <>
            <div className={styles.view}>
                <VncScreen
                    url={url}
                    scaleViewport
                    resizeSession
                    background="#000000"
                    rfbOptions={{
                        credentials: {
                            password: 'password'
                        }
                    }}
                    style={{
                        width: '360px',
                        height: '266px',
                    }}
                />
                {/* <iframe title="" width="900" height="760" src={url} frameBorder="0" /> */}
                {name} {group}
            </div>
        </>
    )
}

export default RDPView
