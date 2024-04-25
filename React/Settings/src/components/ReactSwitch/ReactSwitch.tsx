import React from 'react';
import * as Switch from '@radix-ui/react-switch';
import styles from './styles.module.scss';


export default function ReactSwitch() {

    const [collectData, setCollectData] = React.useState<boolean>()

    return (
        <>
            <label className="Label" htmlFor='dataCollect'>
                Collect additional data
            </label>
            <Switch.Root onCheckedChange={(c) => setCollectData(c)} id="dataCollect" className={styles.SwitchRoot}>
                <Switch.Thumb className={styles.SwitchThumb} />
            </Switch.Root>
        </>
        
    )
    
}
