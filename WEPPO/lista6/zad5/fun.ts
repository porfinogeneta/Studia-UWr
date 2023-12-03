import { Person } from "./user_admin";

function logPerson(person: Person) {
    let additionalInformation: string;
    if (person.role) {
        additionalInformation = person.role;
    } else {
        // używamy jako defaulotwej wartości pustego string'a
        additionalInformation = person.occupation ?? '';
    }
        console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
    }