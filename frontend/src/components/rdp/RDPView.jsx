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
                        width: '800px',
                        height: '600px',
                    }}
                />
                {name} {group}
            </div>
        </>
    )
}

export default RDPView
