export interface Process {
  name: string;
  arrivalTime: number;
  burstTime: number;
  priority: number;
}

export interface ProcessResult extends Process {
  completionTime: number;
  turnaroundTime: number;
  waitingTime: number;
}

/**
 * Pretty prints tabularized data.
 *
 * @param headers the headers of the table
 * @param data an array of objects, representing the rows of the table (if a row is missing, an empty string will be displayed instead)
 */
function printTable(headers: string[], data: Record<string, any>[]) {
  const formattedData = data.map((row) =>
    headers.reduce((acc, header) => {
      acc[header] = row[header] ?? '';
      return acc;
    }, {} as Record<string, any>)
  );

  console.table(formattedData, headers);
}

/**
 * Pretty prints a Gantt Chart for CPU processes.
 *
 * @param tasks the CPU processes and their start & end times (in CPU cycles)
 */
function printGanttChart(
  tasks: { name: string; start: number; end: number }[]
) {
  const START_PADDING = 4;

  const maxEnd = tasks[tasks.length - 1].end;
  const timeUnitWidth = 3;
  const totalWidth = (maxEnd + 1) * timeUnitWidth;

  const cycleLabels = Array.from({ length: maxEnd + 1 }, (_, i) =>
    i.toString().padEnd(timeUnitWidth)
  );
  const topCycleAxis = ' '.repeat(START_PADDING) + cycleLabels.join('');
  const bottomCycleAxis = ' '.repeat(START_PADDING) + cycleLabels.join('');
  const separatorLine = ' '.repeat(START_PADDING) + '•'.repeat(totalWidth);

  console.log(topCycleAxis);
  console.log(separatorLine);

  tasks.forEach((task) => {
    const startOffset = task.start * timeUnitWidth;
    const taskWidth = (task.end - task.start) * timeUnitWidth;

    const nameColumn = task.name.padEnd(START_PADDING);
    const taskBar = ' '.repeat(startOffset) + '█'.repeat(taskWidth);
    const durationLabel = `(${task.end - task.start})`.padStart(1);

    console.log(`${nameColumn}${taskBar} ${durationLabel}`);
  });

  console.log(separatorLine);
  console.log(bottomCycleAxis);
}

/**
 * Displays the Waiting Time calculations and prints the Average Waiting Time.
 *
 * @param results the process results after running the scheduling algorithm
 */
function printFormula(results: ProcessResult[]) {
  let totalWaitingTime = 0;

  results.forEach((result) => {
    const waitingTime = result.waitingTime;
    const completionTime = result.completionTime;
    const burstTime = result.burstTime;

    // Calculate waiting time based on completion and burst times
    const waitingTimeFormula = `${completionTime} - ${result.arrivalTime} - ${burstTime}`;
    console.log(`WT_${result.name} = ${waitingTimeFormula} = ${waitingTime}ms`);

    totalWaitingTime += waitingTime;
  });

  const averageWaitingTime = totalWaitingTime / results.length;

  console.log(
    `\nThe average waiting time is\n(${results
      .map((r) => r.waitingTime)
      .join(' + ')})/${results.length} = ${totalWaitingTime}/${
      results.length
    } = ${averageWaitingTime.toFixed(1)}ms`
  );
}

/**
 * Pretty prints & formats the results.
 *
 * @param results
 */
export function printResults(results: ProcessResult[]) {
  // Display results in table format
  printTable(
    [
      'Process',
      'Arrival Time',
      'Burst Time',
      'Completion Time',
      'Turnaround Time',
      'Waiting Time',
    ],
    results.map((result) => ({
      Process: result.name,
      'Arrival Time': result.arrivalTime,
      'Burst Time': result.burstTime,
      'Completion Time': result.completionTime,
      'Turnaround Time': result.turnaroundTime,
      'Waiting Time': result.waitingTime,
    }))
  );

  console.log('\n');

  // Prepare data for Gantt chart
  const ganttData = results.map((result) => ({
    name: result.name,
    start: result.completionTime - result.burstTime,
    end: result.completionTime,
  }));

  printGanttChart(ganttData);

  console.log('\n');

  // Print formula & average waiting time
  printFormula(results);
}
