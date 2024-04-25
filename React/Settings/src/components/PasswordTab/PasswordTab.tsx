import React from "react";

import "../../modules/utils.scss"

export default function PasswordTab() {

    const [currentPassword, setCurrentPassword] = React.useState<string>("")
    const [newPassword, setNewPassword] = React.useState<string>("")
    const [confirmPassword, setConfirmPassword] = React.useState<string>("")


    return (
        <>
            <p className="Text">Change your password here. After saving, you'll be logged out.</p>
            <fieldset className="Fieldset">
                <label className="Label" htmlFor="currentPassword">
                    Current password
                </label>
                <input className="Input" id="currentPassword" type="password" value={currentPassword} />
            </fieldset>
            <fieldset className="Fieldset">
                <label className="Label" htmlFor="newPassword">
                    New password
                </label>
                <input onChange={(e) => setNewPassword(e.target.value)} className="Input" id="newPassword" type="password" value={newPassword} />
            </fieldset>
            <fieldset className="Fieldset">
                <label className="Label" htmlFor="confirmPassword">
                    Confirm password
                </label>
                <input onChange={(e) => setConfirmPassword(e.target.value)} className="Input" id="confirmPassword" type="password" value={confirmPassword}/>
            </fieldset>
            <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end' }}>
                <button className="Button green">Change password</button>
            </div>

        </>
    )
}