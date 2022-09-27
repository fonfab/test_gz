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

export interface IDealType extends IId {
  name: string,
}

export interface IInventory extends IId {
  name: string,
}

export interface IDestinationPlace extends IId {
  name: string,
}

export interface ICounterparty extends IId {
  name: string,
  rating: IRating,
  rating_id: number,
}


export interface IDeal extends IId {
  type: IDealType,
  amount: number,
  cost: number,
  counterparty: ICounterparty,
  inventory: IInventory,
  destination_place: IDestinationPlace,

  deal_date: string,
  start_date: string,
  end_date: string,
}
