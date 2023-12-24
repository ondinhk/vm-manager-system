import styles from './styles.module.css'
import { VncScreen } from 'react-vnc';

const RDPView = ({ name, url }) => {
    return (
        <>
            <div className={styles.view}>
                <VncScreen
                    url={url}
                    scaleViewport
                    background="#000000"
                    rfbOptions={{
                        credentials: {
                            password: 'password'
                        }
                    }}
                    style={{
                        width: '640px',
                        height: '480px',
                    }}
                />
                {name}
            </div>
        </>
    )
}

export default RDPView
