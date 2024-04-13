import {TeamMemberType} from "../../types/CompanyData"
import classes from "./styles.module.scss"

export default function TeamCard({darkMode, member}: {darkMode: boolean, member: TeamMemberType}){
    return (
        <div className={`${darkMode ? classes.dark_theme : classes.light_theme} ${classes.team_member}`}>
            <img src={member.image} alt={member.name} />
            <div>
                <h3>{member.name}</h3>
                <p>{member.position}</p>
                <p>{member.bio}</p>
            </div>
        </div>            
    )
}