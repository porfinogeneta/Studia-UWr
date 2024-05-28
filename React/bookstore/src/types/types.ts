export type Book = {
    id: string;
    title: string;
    author: string;
    copies: number;
    description: string;
    genre: Genre;
    genreId: string;
    price: number;
    year: string;
    currency: string | never
}


export type Genre = {
    id: string;
    name: string;
  }