import type { Process, ProcessResult } from '../shared';

export function firstComeFirstServe(processes: Process[]): ProcessResult[] {
  // Sort processes by arrival time to ensure FCFS
  processes.sort((a, b) => a.arrivalTime - b.arrivalTime);

  let currentTime = 0; // The current CPU clock cycle

  const results: ProcessResult[] = processes.map((process) => {
    const startTime = Math.max(currentTime, process.arrivalTime);
    const completionTime = startTime + process.burstTime;
    const turnaroundTime = completionTime - process.arrivalTime;
    const waitingTime = turnaroundTime - process.burstTime;

    currentTime = completionTime;

    return {
      ...process,
      completionTime,
      turnaroundTime,
      waitingTime,
    };
  });

  return results;
}
