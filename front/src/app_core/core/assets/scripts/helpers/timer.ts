/** Timer class */
export class Timer {
  timestamp: number;
  moduleName: string;
  moduleDescription: string;

  /** Конструктор
   * @param {String} name - Название модуля
   * @param {String} description - Описание модуля
   * */
  constructor(name: string, description: string) {
    this.timestamp = performance.now();
    this.moduleName = name;
    this.moduleDescription = description;
  }

  /** Timer end
   *  @return {number}
   * */
  end(): number {
    return performance.now() - this.timestamp;
  }

  /** Timer end log to doRequest */
  endWithLogToDoRequest(): void {
    const time = Math.round(this.end());
    const logData = [this.moduleName, time, this.moduleDescription];

    if (time < 1000) console.log(...logData);
    else if (time < 2000) console.warn(...logData);
    else console.error(...logData);
  }
}

export const formatToLocaleTime = (date: Date) => {
  const timezoneDiff = new Date().getTimezoneOffset()*-60000;
  return new Date(date.getTime() + timezoneDiff);
};
