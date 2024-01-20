import styles from './styles.module.css'
import { VncScreen } from 'react-vnc';

const RDPView = ({ name, group, url }) => {
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
                        width: '300px',
                        height: '230px',
                    }}
                />
                {name} {group}
            </div>
        </>
    )
}

export default RDPView
