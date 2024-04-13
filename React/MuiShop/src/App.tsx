
import { ThemeProvider, createTheme } from '@mui/material'
import './App.css'

import Box from '@mui/material/Box'



// components
import Header from './components/Header'
import Table from './components/Table'


const theme = createTheme({
  palette: {
    primary: {
      main: '#131516'
    }
  }
})


function App() {

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{bgcolor: 'primary.main'}}>
        <Header/>
        <Table/>
      </Box>
      
    </ThemeProvider>
      
  )
}

export default App
