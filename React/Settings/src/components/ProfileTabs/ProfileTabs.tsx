import React from 'react';
import * as Tabs from '@radix-ui/react-tabs';
import styles from './styles.module.scss'

import PasswordTab from '../PasswordTab/PasswordTab';
import PreferencesTab from '../PreferencesTab/PreferencesTab';
import AccountTab from '../AccountTab/AccountTab';

const tabs = [
  {value: "account", name: "Account"},
  {value: "password", name: "Password"},
  {value: "preferences", name: "Preferences"},
]

export default function ProfileTabs() {

  return (
    <Tabs.Root orientation="vertical" className={styles.TabsRoot} defaultValue="account" >
      <Tabs.List className={styles.TabsList} aria-label="Manage your account">
        {tabs.map((tab, idx) => (
          <Tabs.Trigger key={idx} className={styles.TabsTrigger} value={tab.value}>
            {tab.name}
          </Tabs.Trigger>
        ))}
      </Tabs.List>
      <Tabs.Content className={styles.TabsContent} value="account">
        <AccountTab/>
      </Tabs.Content>
      <Tabs.Content className={styles.TabsContent} value="password">
        <PasswordTab/>
      </Tabs.Content>
      <Tabs.Content className={styles.TabsContent} value="preferences">
        <PreferencesTab/>
      </Tabs.Content>
    </Tabs.Root>
  )
};
