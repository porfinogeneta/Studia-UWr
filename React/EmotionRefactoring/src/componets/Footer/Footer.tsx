import styled from "@emotion/styled"

const FooterStyle = styled.footer(`
    padding: 20px 0;
    text-align: center;
`)


export default function Footer({name}: {name: string}){
    return (
        <FooterStyle>
            <div>
                <p>
                    &copy; {new Date().getFullYear()} {name}
                </p>
            </div>
        </FooterStyle>
    )
}