import { ReactNode } from "react";
import styled from "@emotion/styled"


const SectionStyle = styled.section`
  padding: 20px 0;
  :nth-child(even) {
    background-color: ${props => props.theme.sectionEvenBg};
  }
`

const SectionContentStyle = styled.div`
  max-width: 800px;
  margin: 0 auto;

  h2 {
    font-size: 2.5em;
    margin-bottom: 20px;
    display: inline-block;
  }
`

export default function Section({id, title, children}: {id: string, title: string, children: ReactNode}) {
    return (
      <SectionStyle id={id}>
          <SectionContentStyle>
            <h2>{title}</h2>
            {children}
          </SectionContentStyle>
      </SectionStyle>
    )
}