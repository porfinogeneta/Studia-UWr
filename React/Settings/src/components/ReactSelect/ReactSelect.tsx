import React from "react";
import * as Select from '@radix-ui/react-select';
import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from '@radix-ui/react-icons';

import styles from "./styles.module.scss"
import "../../modules/utils.scss"

const SelectItem = React.forwardRef<
  React.ComponentRef<typeof Select.Item>,
  React.ComponentPropsWithoutRef<typeof Select.Item>
>(({ children, ...props }, forwardedRef) => {
  return (
    <Select.Item className={styles.SelectItem} {...props} ref={forwardedRef}>
      <Select.ItemText>{children}</Select.ItemText>
      <Select.ItemIndicator className={styles.SelectItemIndicator}>
        <CheckIcon />
      </Select.ItemIndicator>
    </Select.Item>
  );
});


export default function ReactSelect() {


    const selectItemRef = React.useRef<HTMLDivElement>(null)

    const focusSelectItemRef = () => {
      selectItemRef.current ? selectItemRef.current.focus() : ''
    }

    const [selected, setSelected] = React.useState("")
    

    return (
      <>
        <label className="Label" htmlFor="notifications">
          Notification Settings
        </label>
        <Select.Root onValueChange={(e) => setSelected(e)} value={selected}>
          <Select.Trigger className={styles.SelectTrigger} aria-label="Notifications">
              <Select.Value/>
              <Select.Icon className={styles.SelectIcon}>
                  <ChevronDownIcon />
              </Select.Icon>
          </Select.Trigger>
          <Select.Portal>
              <Select.Content className={styles.SelectContent}>
                  <Select.ScrollUpButton className={styles.SelectScrollButton}>
                      <ChevronUpIcon />
                  </Select.ScrollUpButton>
                  <Select.Viewport className={styles.SelectViewport}>
                      <Select.Group>
                        <SelectItem value="All">All</SelectItem>
                        <SelectItem value="Only Followed">Only Followed</SelectItem>
                        <SelectItem ref={selectItemRef} value="None">None</SelectItem>
                      </Select.Group>
                  </Select.Viewport>
                  <Select.ScrollDownButton className={styles.SelectScrollButton}>
                      <ChevronDownIcon />
                  </Select.ScrollDownButton>
              </Select.Content>
            </Select.Portal>
        </Select.Root>
        {/* <button className="Button green" onClick={focusSelectItemRef}>Focus</button> */}
      </>
    )
}