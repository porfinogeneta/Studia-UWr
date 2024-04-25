import React from 'react';
import * as Avatar from '@radix-ui/react-avatar';
import styles from "./styles.module.scss"
import "../../modules/utils.scss"

export default function ReactAvatar() {


    const handleAvatarClick = () => {
        const avatarUploadInput = document.getElementById('avatarUpload')
        avatarUploadInput ? avatarUploadInput.click() : ''
    }

    return (

   <fieldset>
        <label className="Label" htmlFor="avatarUpload" onClick={handleAvatarClick}>
            <button>Avatar</button>
        </label>
        <div style={{ display: 'flex', gap: 20 }} onClick={handleAvatarClick}>
            <input
                type="file"
                accept="image/*"
                style={{ display: 'none' }}
                id="avatarUpload"
            />
            <Avatar.Root className={styles.AvatarRoot}>
                <Avatar.Image
                    className={styles.AvatarImage}
                    src="https://images.unsplash.com/photo-1492633423870-43d1cd2775eb?&w=128&h=128&dpr=2&q=80"
                    alt="Colm Tuite"
                />
                <Avatar.Fallback className={styles.AvatarFallback} delayMs={600}>
                    CT
                </Avatar.Fallback>
            </Avatar.Root>
        </div>
   </fieldset>
    
   )
};

