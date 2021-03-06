import request from '@/utils/request'

/**
 * @param send data
 */
export function getAllHouse(url,params) {
  // http://127.0.0.1:8000/v1/api/all_house/?page=2
  return request({
    url: url,
    method: 'get',
    params
  })
}

// export function getPotion(params) {
//   return request({
//     url: '/position/',
//     method: 'get',
//     params
//   })
// }

// 排序
export function getOrderHouse(params) {
  return request({
    // url: '/all_house/?ordering='+ methods + '&search='+ search +'&page=' + num,
    url: '/all_house/',
    method: 'get',
    params
  })
}

export function getAll(community,num,params) {
  return request({
    url: '/all_house/?search='+community+'&page='+num,
    method: 'get',
    params
  })
}

export function getIndex(params) {
  return request({
    url: '/index',
    method: 'get',
    params
  })
}

export function getRegionInfo(id,params) {
  return request({
    url: '/region/'+id,
    method: 'get',
    params
  })
}

export function getEelevatorInfo(params) {
  return request({
    url: '/elevator',
    method: 'get',
    params
  })
}

export function getConstructureInfo(params) {
  return request({
    url: '/constrcture',
    method: 'get',
    params
  })
}

export function getPurposeInfo(params) {
  return request({
    url: '/purpose',
    method: 'get',
    params
  })
}

export function getDecorationInfo(params) {
  return request({
    url: '/decoration',
    method: 'get',
    params
  })
}

export function getFloorInfo(params) {
  return request({
    url: '/floor',
    method: 'get',
    params
  })
}

export function getLayoutInfo(params) {
  return request({
    url: '/layout',
    method: 'get',
    params
  })
}

export function getOrientationInfo(params) {
  return request({
    url: '/oritentation',
    method: 'get',
    params
  })
}

export function getCommunityInfo(params) {
  return request({
    url: '/community',
    method: 'get',
    params
  })
}

export function getAllCommunityInfo(params) {
  return request({
    url: '/allcommunity/',
    method: 'get',
    params
  })
}

export function getCommunityRangeInfo(params) {
  return request({
    url: '/communityrange',
    method: 'get',
    params
  })
}
