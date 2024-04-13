export type Order = 'asc' | 'desc';

export interface Data {
    id: number;
    name: string;
    type: string;
    price: number;
    currency: string;
    available: boolean;
    quantity: number;
  }