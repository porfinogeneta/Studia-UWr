import { Person, persons } from "./user_admin";

// sprawdzamy czy mamy pole role, czy occupation
export function isAdmin(person: Person): person is (Person & {role: string}){
    return 'role' in person;
}
export function isUser(person: Person): person is (Person & {occupation: string}) {
    return 'occupation' in person;
}

export function logPerson(person: Person) {
    let additionalInformation: string = '';
    if (isAdmin(person)) {
        additionalInformation = person.role;
    }
    if (isUser(person)) {
        additionalInformation = person.occupation;
    }
    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`)
};

console.log(logPerson(persons[0]));
