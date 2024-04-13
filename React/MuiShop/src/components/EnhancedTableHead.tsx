import { TableHead, TableRow, TableCell, TableSortLabel, Box } from "@mui/material";
import { visuallyHidden } from '@mui/utils';
import { Order, Data } from "../types/types";


interface EnhancedTableProps {
    onRequestSort: (event: React.MouseEvent<unknown>, property: keyof Data) => void;
    order: Order;
    orderBy: string;
    currency: string
  }

interface HeadCell {
    disablePadding: boolean;
    id: keyof Data | 'action';
    label: string;
    numeric: boolean;
  }

  const headCells: readonly HeadCell[] = [
    {
      id: 'name',
      numeric: false,
      disablePadding: true,
      label: 'Name',
    },
    {
      id: 'type',
      numeric: false,
      disablePadding: false,
      label: 'Type',
    },
    {
      id: 'price',
      numeric: true,
      disablePadding: false,
      label: 'Price',
    },
    {
      id: 'available',
      numeric: false,
      disablePadding: false,
      label: 'Available',
    },
    {
      id: 'quantity',
      numeric: true,
      disablePadding: false,
      label: 'Quantity',
    },
    {
      id: 'action',
      numeric: true,
      disablePadding: false,
      label: 'Action',
    },
  ];

const cellStyle = {
    color: ((theme) => theme.palette.primary.contrastText)
}

export default function EnhancedTableHead(props: EnhancedTableProps) {
    const { order, orderBy, onRequestSort, currency } = props;
    
      const createSortHandler =
      (property: keyof Data | "action") => (event: React.MouseEvent<unknown>) => {
        if (property !== 'action') {
            onRequestSort(event, property);
        }
      };
  
    return (
      <TableHead>
        <TableRow sx={{backgroundColor: 'grey'}}>
          {headCells.map((headCell) => (
            <TableCell
              key={headCell.id}
              align={headCell.id != 'action' ? 'left' : 'right'}
              padding={headCell.disablePadding ? 'none' : 'normal'}
              sortDirection={orderBy === headCell.id ? order : false}
              // sx={cellStyle}
            >
            {headCell.id !== 'action' ? (
                 < TableSortLabel
                    active={orderBy === headCell.id}
                    direction={orderBy === headCell.id ? order : 'asc'}
                    onClick={createSortHandler(headCell.id)}
                >
                    {headCell.id != 'price' ? headCell.label : `${headCell.label} (${currency})`}
                    {orderBy === headCell.id ? (
                    <Box component="span" sx={visuallyHidden}>
                        {order === 'desc' ? 'sorted descending' : 'sorted ascending'}
                    </Box>
                    ) : null}
                </TableSortLabel>
            ) : <span>{headCell.label}</span>}
             
            </TableCell>
          ))}
        </TableRow>
      </TableHead>
    );
  }