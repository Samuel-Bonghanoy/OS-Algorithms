import { Process, printResults } from './shared';
import schedule from './algorithms';

const processes: Process[] = [
  { name: 'A', arrivalTime: 0, burstTime: 4, priority: 2 },
  { name: 'B', arrivalTime: 1, burstTime: 3, priority: 1 },
  { name: 'C', arrivalTime: 2, burstTime: 1, priority: 3 },
  { name: 'D', arrivalTime: 3, burstTime: 2, priority: 1 },
];

const result = schedule.priorityNonPreemptive(processes);

printResults(result);
