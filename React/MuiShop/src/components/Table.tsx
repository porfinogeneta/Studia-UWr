import * as React from 'react';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import Fab from '@mui/material/Fab';
import AddIcon from '@mui/icons-material/Add';
import styled from '@emotion/styled/macro';

import {Order, Data} from '../types/types'


import EnhancedTableHead from './EnhancedTableHead';
import Notification from './Notification';
import FormAddModal from './FormAddModal';


function createData(
    id: number,
    name: string,
    type: string,
    price: number,
    currency: string,
    available: boolean,
    quantity: number
): Data {
  return {
    id,
    name,
    type,
    price,
    currency,
    available,
    quantity
  };
}

const rows = [
    createData(1, 'Cupcake', 'Type 1', 3.7, 'PLN', true, 4),
    createData(2, 'Donut', 'Type 2', 2.5, 'PLN', false, 6),
    createData(3, 'Eclair', 'Type 3', 4.2, 'PLN', true, 8),
    createData(4, 'Froyo', 'Type 4', 1.8, 'PLN', false, 3),
    createData(5, 'Gingerbread', 'Type 5', 5.1, 'PLN', true, 5),
    createData(6, 'Honeycomb', 'Type 6', 3.9, 'PLN', false, 2),
    createData(7, 'Ice Cream Sandwich', 'Type 7', 6.4, 'PLN', true, 7),
    createData(8, 'Jelly Bean', 'Type 8', 2.3, 'PLN', true, 9),
    createData(9, 'KitKat', 'Type 9', 4.7, 'PLN', false, 1),
    createData(10, 'Lollipop', 'Type 10', 3.1, 'PLN', true, 10),
    createData(11, 'Marshmallow', 'Type 11', 4.5, 'PLN', true, 6),
    createData(12, 'Nougat', 'Type 12', 3.8, 'PLN', false, 2),
    createData(13, 'Oreo', 'Type 13', 5.2, 'PLN', true, 8),
    createData(14, 'Pie', 'Type 14', 6.1, 'PLN', false, 4),
    createData(15, 'Android 10', 'Type 15', 7.3, 'PLN', true, 5),
    createData(15, 'iPhone', 'Type 1', 7.3, 'EUR', true, 5)
];

function descendingComparator<T>(a: T, b: T, orderBy: keyof T) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}



function getComparator<Key extends keyof any>(
  order: Order,
  orderBy: Key,
): (
  a: { [key in Key]: number | string },
  b: { [key in Key]: number | string },
) => number {
  return order === 'desc'
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy);
}

const cellStyle = {
    color: ((theme) => theme.palette.primary.contrastText)
}

export default function EnhancedTable() {
  const [order, setOrder] = React.useState<Order>('asc');
  const [orderBy, setOrderBy] = React.useState<keyof Data>('name');
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);
  const [appRows, setAppRows] = React.useState(rows);
  const [openNotification, setOpenNotification] = React.useState<boolean>(false);
  const [currency, setCurrency] = React.useState<string>('PLN');
  const [modalOpen, setModalOpen] = React.useState<boolean>(false);

  const handleRequestSort = (
    event: React.MouseEvent<unknown>,
    property: keyof Data,
  ) => {
    const isAsc = orderBy === property && order === 'asc';
    setOrder(isAsc ? 'desc' : 'asc');
    setOrderBy(property);
  };


  const handleClick = (id: number) => {
    const updatedRows = appRows.filter(r => r.id != id)
    setAppRows(updatedRows)
    setOpenNotification(true)
  };


  // zmiana liczby wierszy per strona
  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    // przerabiamy string na inta i ustawiamy stronę na 0
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };



  // Avoid a layout jump when reaching the last page with empty rows.
  const emptyRows =
    page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;

  const visibleRows = () => {
    if (page * rowsPerPage >= appRows.length){
        setPage(page => page > 0 ? page - 1 : 0)
    }
    return appRows.slice().sort(getComparator(order, orderBy)).slice(
        page * rowsPerPage,
        page * rowsPerPage + rowsPerPage,
    )
  }


  const handleModal = () => {
    setModalOpen(prev => !prev)
  }



  return (
    <Box sx={{ width: '70%', margin: 'auto'}}>
      <Paper sx={{ width: '100%', mb: 2, mt: 4, backgroundColor: (theme) => theme.palette.primary.main}}>
        <TableContainer sx={{display: 'flex', justifyContent: 'center', color: 'white'}}>
          <Table
            sx={{ maxWidth: 750 }}
            aria-labelledby="tableTitle"
            size={'medium'}
          >
            <EnhancedTableHead
              order={order}
              orderBy={orderBy}
              onRequestSort={handleRequestSort}
              currency={currency}
            />
            <TableBody>
              {visibleRows().map((row) => {
                return (
                  <TableRow
                    hover
                    key={row.id}
                    sx={{ cursor: 'pointer'}}
                  >
                    <TableCell sx={cellStyle} align="left">{row.name}</TableCell>
                    <TableCell sx={cellStyle} align="left">{row.type}</TableCell>
                    <TableCell sx={cellStyle} align="left">{row.price} {row.currency}</TableCell>
                    <TableCell sx={cellStyle} align="left">{row.available ? "True" : "False"}</TableCell>
                    <TableCell sx={cellStyle} align="left">{row.quantity}</TableCell>
                    <TableCell align="right">
                        <IconButton onClick={() => handleClick(row.id)} color='warning' size='small'>
                            <DeleteIcon />
                        </IconButton>
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[5, 10, 25]}
          component="div"
          count={appRows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={handleChangePage}
          onRowsPerPageChange={handleChangeRowsPerPage}
          sx={cellStyle}
        />
        <Notification
            open={openNotification}
            handleCloseNotification={() => setOpenNotification(false)}
        />
        <Fab onClick={handleModal} sx={{position: 'absolute', bottom: '20px', right: '20px'}} color='secondary' aria-label="add">
            <AddIcon/>
        </Fab>
        <FormAddModal rows={appRows} open={modalOpen} handleModal={handleModal}/>
      </Paper>
    </Box>
  );
}