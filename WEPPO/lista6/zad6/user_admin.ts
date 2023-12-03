type User = {
    type: string
    name: string;
    age: number;
    occupation: string;
}
type Admin = {
    type: string,
    name: string;
    age: number;
    role: string;
}
export type Person = User | Admin;
    
export const persons: Person[] = [
{
    type: 'user',
    name: 'Jan Kowalski',
    age: 17,
    occupation: 'Student'
},
{
    type: 'admin',
    name: 'Tomasz Malinowski',
    age: 20,
    role: 'Administrator'
}];