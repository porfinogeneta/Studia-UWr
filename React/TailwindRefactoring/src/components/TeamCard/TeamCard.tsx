import {TeamMemberType} from "../../types/CompanyData"


export default function TeamCard({member}: {member: TeamMemberType}){
    
    return (
        <div className="flex-0 w-[calc(33.33%-20px)] p-5 m-3 bg-gray-100 dark:bg-gray-600 text-center">
            <img src={member.image} alt={member.name} className="rounded-full mb-4 mx-auto" />
            <div>
                <h3 className="text-lg font-semibold mb-2">{member.name}</h3>
                <p className="text-md mb-2">{member.position}</p>
                <p className="text-md">{member.bio}</p>
            </div>
        </div>
            
    )
}