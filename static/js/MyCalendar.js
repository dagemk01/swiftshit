import React, { useState } from 'react';
import { Calendar } from '@material-ui/pickers';

function MyCalendar() {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <Calendar
      value={selectedDate}
      onChange={date => setSelectedDate(date)}
    />
  );
}

function App() {
  return (
    <div>
      <MyCalendar />
    </div>
  );
}

export default App;