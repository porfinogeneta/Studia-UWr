import {TeamMemberType} from "../../types/CompanyData"


import styled from "@emotion/styled"

const TeamCardStyle = styled.div`
    flex: 0 0 calc(33.33% - 20px);
    padding: 20px;
    margin: 10px;
    text-align: center;

    img {
        border-radius: 50%;
        margin-bottom: 20px;
    }

    h3 {
        margin-bottom: 10px;
        display: inline-block;
    }

    background-color: ${props => props.theme.teamMemberBg};
    color: ${props => props.theme.text};
`

export default function TeamCard({member}: {member: TeamMemberType}){
    
    return (
        <TeamCardStyle>
            <img src={member.image} alt={member.name} />
            <div>
                <h3>{member.name}</h3>
                <p>{member.position}</p>
                <p>{member.bio}</p>
            </div>
        </TeamCardStyle>
            
    )
}