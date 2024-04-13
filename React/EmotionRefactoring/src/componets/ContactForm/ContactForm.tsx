import styled from "@emotion/styled"


const ContactFormStyle = styled.form`
    max-width: 500px;
    margin: 0 auto;
    margin-bottom: 40px;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
  
    input[type="text"],
    input[type="email"],
    textarea {
      width: calc(100% - 20px);
      padding: 10px;
      border-radius: 5px;
      border: none;
      margin-top: 5px;
      background-color: ${props => props.theme.contactInputBg};
      color: ${props => props.theme.text};
      border: 1px solid ${props => props.theme.contactInputBorder};
    }
  
    textarea {
      resize: vertical;
    }

    background-color: ${props => props.theme.contactBg};
    color: ${props => props.theme.text};
    border: 1px solid ${props => props.theme.contactBorder};
`


const ContactButtonStyle = styled.button`
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    background-color: ${props => props.theme.contactBtnBg};
    color: ${props => props.theme.btnColoredTxt};

    :hover {
      background-color: ${props => props.theme.contactBtnBgHover};
    }
`

const FormGroupStyle = styled.div`
    margin-bottom: 20px;
`

export default function ContactForm() {

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
      };

    return (
        <ContactFormStyle onSubmit={handleSubmit}>
            <FormGroupStyle>
                <input type="text" placeholder="Name" required />
            </FormGroupStyle>
            <FormGroupStyle>
                <input type="email" placeholder="Email" required />
            </FormGroupStyle>
            <FormGroupStyle>
                <textarea rows={5} placeholder="Message" required></textarea>
            </FormGroupStyle>
            <ContactButtonStyle type="submit">Send Message</ContactButtonStyle>
        </ContactFormStyle>
        
    )
}