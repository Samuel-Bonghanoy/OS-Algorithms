import type { Process, ProcessResult } from '../shared';

export function shortestJobFirst(processes: Process[]): ProcessResult[] {
  // Sort processes by arrival time initially
  processes.sort((a, b) => a.arrivalTime - b.arrivalTime);

  let currentTime = 0; // The current CPU clock cycle
  const results: ProcessResult[] = [];

  // Array to keep track of processes that are ready to execute
  const readyQueue: Process[] = [];

  while (processes.length > 0 || readyQueue.length > 0) {
    // Add all processes that have arrived by the current time to the ready queue
    while (processes.length > 0 && processes[0].arrivalTime <= currentTime) {
      readyQueue.push(processes.shift()!); // Move the process to the ready queue
    }

    if (readyQueue.length > 0) {
      // Sort the ready queue by burst time (shortest job first)
      readyQueue.sort((a, b) => a.burstTime - b.burstTime);

      // Select the process with the shortest burst time
      const currentProcess = readyQueue.shift()!;

      const startTime = Math.max(currentTime, currentProcess.arrivalTime);
      const completionTime = startTime + currentProcess.burstTime;
      const turnaroundTime = completionTime - currentProcess.arrivalTime;
      const waitingTime = turnaroundTime - currentProcess.burstTime;

      // Update the current time to the completion time of the current process
      currentTime = completionTime;

      results.push({
        ...currentProcess,
        completionTime,
        turnaroundTime,
        waitingTime,
      });
    } else {
      // If no processes are ready, move time forward to the next process arrival
      currentTime = processes[0].arrivalTime;
    }
  }

  return results;
}
