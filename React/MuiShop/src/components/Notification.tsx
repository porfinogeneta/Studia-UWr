import * as React from 'react';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
import Box from '@mui/material/Box';

export default function Notification({open, handleCloseNotification}: {open: boolean, handleCloseNotification: () => void}) {


  const handleClose = (event?: React.SyntheticEvent | Event, reason?: string) => {
    if (reason === 'clickaway') {
      return;
    }

    handleCloseNotification();
  };

  return (
    <Box sx={{position: 'absolute', bottom: '10px'}}>
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
        <Alert
          onClose={handleClose}
          severity="success"
          variant="filled"
          sx={{ width: '100%' }}
        >
          Deleted!
        </Alert>
      </Snackbar>
    </Box>
  );
}