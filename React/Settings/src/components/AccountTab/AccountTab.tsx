import React from "react";


import ReactRadioGroup from '../ReactRadioGroup/ReactRadioGroup';
import DeleteModal from "../DeleteModal/DeleteModal";

import '../../modules/utils.scss'
import ReactAvatar from "../ReactAvatar/ReactAvatar";


export default function AccountTab() {

    const [name, setName] = React.useState<string>("Pedro Duarte")
    const [username, setUsername] = React.useState<string>("@peduarte")

    return (
        <>      
            <p className="Text">Make changes to your account here. Click save when you're done.</p>
            <ReactAvatar/>
            <fieldset className="Fieldset">
                <label className="Label" htmlFor="name">
                    Name
                </label>
                <input onChange={(e) => setName(e.target.value)} className="Input" id="name" defaultValue={name} />
            </fieldset>
            <fieldset className="Fieldset">
                <label className="Label" htmlFor="username">
                Username
                </label>
                <input className="Input" onChange={(e) => setUsername(e.target.value)} id="username" defaultValue={username} />
            </fieldset>
            <ReactRadioGroup/>
            <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end', gap: '16px' }}>
                <DeleteModal/>
                <button className="Button green">Save changes</button>
            </div>
        </>
    )
}