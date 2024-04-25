import React from 'react';
import * as Slider from '@radix-ui/react-slider';
import styles from './styles.module.scss'
import "../../modules/utils.scss"

export default function ReactSlider() {

    const [frequency, setFrequency] = React.useState<number>(50)
    

    return (
        <>
            <label className="Label" htmlFor='frequency'>
                Notification Frequency
            </label>
            <Slider.Root onValueChange={(e) => setFrequency(e[0])} id="frequency" 
                className={styles.SliderRoot}
                defaultValue={[frequency]}
                max={100} step={1}>
                <Slider.Track className={styles.SliderTrack}>
                    <Slider.Range className={styles.SliderRange} />
                </Slider.Track>
                <Slider.Thumb className={styles.SliderThumb} aria-label="Volume" />
            </Slider.Root>
        </>
    )
}
