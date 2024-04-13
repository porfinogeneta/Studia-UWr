import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import Typography from '@mui/material/Typography';
import { TextField, styled, MenuItem, Button } from '@mui/material';

import { Data } from '../types/types';

const Types = [
    {
        value: 'Type 1',
        label: 'Type 1'
    },
    {
        value: 'Type 2',
        label: 'Type 2'
    },
    {
        value: 'Type 3',
        label: 'Type 3'
    },
    {
        value: 'Type 4',
        label: 'Type 4'
    }
]

const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 800,
  bgcolor: 'primary.light',
  color: 'primary.contrastText',
  boxShadow: 24,
  p: 4,
};

const StyledTextField = styled(TextField)(({ theme }) => ({
    input: {color: theme.palette.primary.contrastText},
    '& label': {
        color: theme.palette.primary.contrastText
    },
    '& label.Mui-focused': {
        color: theme.palette.primary.contrastText,
    },
    '& .MuiOutlinedInput-root': {
        margin: '8px',
        '& fieldset': {
            color: "red",
            borderColor: theme.palette.primary.contrastText,
        },
    '&:hover fieldset': {
        borderColor: theme.palette.primary.contrastText,
    },
    '&.Mui-focused fieldset': {
        borderColor: theme.palette.primary.contrastText,
    },
    },
  }
));

export default function FormAddModal({ open, handleModal, rows }: { open: boolean; handleModal: () => void, rows: Data[] }) {

    const [name, setName] = React.useState<string>('')
    const [type, setType] = React.useState<string>('Type 1')
    const [price, setPrice] = React.useState<number>(0)
    const [quantity, setQuantity] = React.useState<number>(0)

    const [nameError, setNameError] = React.useState<boolean>(false)
    const [quantityError, setQuantityError] = React.useState<boolean>(false)

    const handleClose = () => {
        handleModal();
    };

    const handleAddProduct = (event) => {
        event.preventDefault()
        if (quantity == 0){
            setQuantityError(true)
        }
        if (name == ''){
            setNameError(true)
        }

        if (quantity && name) {
            const product = {id: Math.random() * 10000, 
                name: name, type: type, price: price,
                 currency: "PLN", available: quantity != 0 ? true : false, quantity: quantity}
    
            rows.push(product)
            setName('')
            setType('')
            setPrice(0)
            setQuantity(0)

            handleClose()
        }else {
            return
        }

        

        
    }

    return (
        <Modal
            aria-labelledby="transition-modal-title"
            aria-describedby="transition-modal-description"
            open={open}
            onClose={handleClose}
            closeAfterTransition
            slots={{ backdrop: Backdrop }}
            slotProps={{
                backdrop: {
                timeout: 500,
                },
            }}
        >
        <Fade in={open}>
            <Box sx={style}>
            <Typography id="transition-modal-title" variant="h6" component="h2">
                Add product
            </Typography>
            <Box component="form" autoComplete="off" onSubmit={handleAddProduct}>
                <StyledTextField
                fullWidth
                variant="outlined"
                label="Name"
                value={name}
                error={nameError}
                onChange={e => setName(e.target.value)}
                ></StyledTextField>
                <StyledTextField
                fullWidth
                select
                variant="outlined"
                label="Type"
                value={type}
                onChange={e => setType(e.target.value)}
                >
                {Types.map((option) => (
                    <MenuItem key={option.value} value={option.value}>
                        {option.label}
                    </MenuItem>
                ))}
                </StyledTextField>
                <StyledTextField
                fullWidth
                required
                variant="outlined"
                label="Price"
                type='number'
                value={price}
                onChange={e => setPrice(parseInt(e.target.value))}
                ></StyledTextField>
                <StyledTextField
                fullWidth
                required
                variant="outlined"
                type='number'
                label="Quantity"
                error={quantityError}
                value={quantity}
                onChange={e => setQuantity(parseInt(e.target.value))}
                ></StyledTextField>
                <Button type='submit' variant="contained" color="success">
                    Add Product
                </Button>
            </Box>
            </Box>
        </Fade>
        </Modal>
    );
}
