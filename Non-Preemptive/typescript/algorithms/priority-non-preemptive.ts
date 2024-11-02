import type { Process, ProcessResult } from '../shared';

export function priorityNonPreemptive(processes: Process[]): ProcessResult[] {
  // Sort processes by arrival time first
  processes.sort((a, b) => a.arrivalTime - b.arrivalTime);

  let currentTime = 0; // The current CPU clock cycle
  const results: ProcessResult[] = [];

  while (processes.length > 0) {
    // Filter ready processes that have arrived by current time
    const readyQueue = processes.filter((p) => p.arrivalTime <= currentTime);

    if (readyQueue.length > 0) {
      // Sort the ready queue by priority and then by arrival time
      readyQueue.sort(
        (a, b) => a.priority - b.priority || a.arrivalTime - b.arrivalTime
      );

      // Select the highest priority process (lowest priority number)
      const currentProcess = readyQueue[0];

      // Calculate times
      const startTime = Math.max(currentTime, currentProcess.arrivalTime);
      const completionTime = startTime + currentProcess.burstTime;
      const turnaroundTime = completionTime - currentProcess.arrivalTime;
      const waitingTime = turnaroundTime - currentProcess.burstTime;

      // Update current time
      currentTime = completionTime;

      // Store results
      results.push({
        ...currentProcess,
        completionTime,
        turnaroundTime,
        waitingTime,
      });

      // Remove the completed process from the original list
      processes = processes.filter((p) => p !== currentProcess);
    } else {
      // If no processes are ready, move time forward to the next process arrival
      currentTime = Math.min(...processes.map((p) => p.arrivalTime));
    }
  }

  return results;
}
