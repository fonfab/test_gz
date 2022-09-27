export interface IBaseUrls {
  main: string,
}


export enum EColorType {
  GREEN = 'green',
  BLUE = 'blue',
  PURPLE = 'purple'
}

export interface ICardMainStructItem {
  icon: string,
  text: string,
}

export interface ITableRow {
  id: number,
  items: Array<string | number>
}

export interface ITableStruct {
  title: string,
  value: (item: unknown) => string | number,
}


export interface IId {
  id: number,
}

export interface IRating extends IId {
  rating: string,
}

export interface ICounterparty extends IId {
  name: string,
  rating: IRating,
  rating_id: number,
}
