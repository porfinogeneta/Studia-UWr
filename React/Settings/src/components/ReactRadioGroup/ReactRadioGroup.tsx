import React from "react";
import * as RadioGroup from '@radix-ui/react-radio-group';

import styles from './styles.module.scss'
import "../../modules/utils.scss"



export default function ReactRadioGroup() {

    const [gender, setGender] = React.useState<string>("")


    return (
        <fieldset className="Fieldset">
            <RadioGroup.Root className={styles.RadioGroupRoot} onValueChange={(e) => setGender(e)} defaultValue="default" aria-label="View density">
                <p className="Label">Gender</p>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <RadioGroup.Item className={styles.RadioGroupItem} value="male" id="r1">
                        <RadioGroup.Indicator className={styles.RadioGroupIndicator} />
                    </RadioGroup.Item>
                    <label  className='Label'  htmlFor="r1">
                        Male
                    </label>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <RadioGroup.Item className={styles.RadioGroupItem} value="female" id="r2">
                        <RadioGroup.Indicator className={styles.RadioGroupIndicator} />
                    </RadioGroup.Item>
                    <label  className="Label" htmlFor="r2">
                        Female
                    </label>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <RadioGroup.Item className={styles.RadioGroupItem} value="other" id="r3">
                        <RadioGroup.Indicator className={styles.RadioGroupIndicator} />
                    </RadioGroup.Item>
                    <label  className="Label" htmlFor="r3">
                        Other
                    </label>
                </div>
            </RadioGroup.Root>
        </fieldset>
  
    )
}


