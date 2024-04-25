import React from "react";

import "../../modules/utils.scss"

import ReactSelect from "../ReactSelect/ReactSelect";
import ReactSlider from "../ReactSlider/ReactSlider";
import ReactSwitch from "../ReactSwitch/ReactSwitch";

export default function PreferencesTab() {
    return (
        <>
            <p className="Text">Change Preferences here. Click save when you are done.</p>
            <fieldset className="Fieldset">
                <ReactSelect/>
            </fieldset>
            <fieldset className="Fieldset">
                <ReactSlider/> 
            </fieldset>
            <fieldset className="Fieldset">
                <ReactSwitch/>
            </fieldset>
            <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end' }}>
                <button className="Button green">Save Preferences</button>
            </div>
        </>
    )
}