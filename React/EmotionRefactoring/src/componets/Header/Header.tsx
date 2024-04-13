import styled from "@emotion/styled"

const HeaderStyle = styled.header({
    padding: '50px 0',
    textAlign: 'center',
      
    h1: {
        fontSize: '3em',
        marginBottom: '10px'
    },
    
    p: {
        fontSize: '1.5em'
    }
})


export default function Header({children}: {children: {name: string, slogan: string}}){
    return (
        <HeaderStyle id="header">
            <div>
                <h1>{children.name}</h1>
                <p>{children.slogan}</p>
            </div>
        </HeaderStyle>
        
    )
}