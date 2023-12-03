type User = {
    name: string;
    age: number;
    occupation: string;
}
type Admin = {
    name: string;
    age: number;
    role: string;
}
// robimy AND po typach, i robimy z niego typ o wszystkich składowych opcjonalnych 
export type Person = Partial<User & Admin>;

export const persons: Person[] = [
{
    name: 'Jan Kowalski',
    age: 17,
    occupation: 'Student',
},
{
    name: 'Tomasz Malinowski',
    age: 20,
    role: 'Administrator'
}];