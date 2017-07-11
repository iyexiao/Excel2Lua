-- Filename: DB_Enemy.lua
-- Author: auto-created by yexiao`s ParseExcel(to lua) tool.
-- methods: X.getDataById(id), X.getArrDataByField(fieldName, fieldValue)
-- Function: no description.

local keys = {
	"id","roleType","roleSex","roleInfo","isLock","lockItems"
}

local data = {
[1]={1,1,0,"战士",false,{item="1"}},
[2]={2,2,0,"剑客",true,{1,2,3,4}},
[3]={3,3,1,"法师",true,{item="sss",cc="我说”sss”"}},
[4]={4,4,1,"药师",true,{item=true}},
}

cc.exports.DB_Enemy = {}
function DB_Enemy.getDataById(id)
    if not id or type(id) ~= 'number' then return nil end
    local tmp = data[id]
    if not tmp then return nil end
    local tbl = {}
    for k,v in pairs(keys) do
         tbl[v] = tmp[k]
     end
     return tbl
end