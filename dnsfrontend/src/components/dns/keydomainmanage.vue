<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>重点域名管理</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">

          <el-col class="handle-select-input-domain">
            <el-form-item prop="input_domain">
              <el-input placeholder="域名"  size="small" v-model="formFilter.select_domain" clearable @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()">搜索</el-button>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button type="success" @click="addCustomer()" size="small">
                <icon name="add" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px" ></icon>新增
              </el-button>
            </el-form-item>
          </el-col>
          <el-col :span="1.5">
            <el-form-item>
              <el-button size="small" @click="dialogFormUploadVisible = true">
                <icon name="upload" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px"></icon>批量导入</el-button>
            </el-form-item>
          </el-col>

          <el-col :span="1.5">
            <el-form-item>
              <el-button size="small">
<!--                 <a href="./features.vue" download="features.vue" style="text-decoration:none; out-line:none; color:#409EFF"> -->
                <icon name="download" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px; padding-right:5px"></icon>模板下载
<!--                 </a> -->
                </el-button>
            </el-form-item>
          </el-col>

<!--           <el-col :span="1.5">
            <el-form-item>
              <el-button type="danger" plain icon="el-icon-close" size="small" @click="dialogFormUploadVisible = true">选中删除</el-button>
            </el-form-item>
          </el-col> -->

        </el-row>
      </el-form>

      <el-dialog title="导入" :visible.sync="dialogFormUploadVisible">
        <el-upload
          ref="upload"
          :action="uploadDataUrl"
          :multiple="false"
          :limit="1"
          :file-list="fileList"
          :on-success="successUpload"
          :auto-upload="false">
          <el-button slot="trigger" size="small" type="primary" @click="clearUploaded" >选取文件</el-button>
          <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传xlsx文件</div>
        </el-upload>
      </el-dialog>
    </div>

    <el-table
        :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        border
        style="width: 100%;"
        ref="multipleTable"
        size="mini">
      <el-table-column type="selection" width="40" align="center">
      </el-table-column>
<!--       <el-table-column prop="id" label="id" align="center" v-if="false">
      </el-table-column> -->
      <el-table-column prop="domain" label="域名" width="200" align="center">
      </el-table-column>
      <el-table-column prop="legal_ip" label="合法IP" align="center" >
      </el-table-column>
      <el-table-column label="操作" width="160" align="center">
        <template slot-scope="scope">
          <el-button size="mini" type="text" @click="handleEdit(scope.$index, scope.row)">
            <icon name="edit" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon>编辑</el-button>
          <el-button size="mini" type="text" @click="handleDelete(scope.row)">
            <icon name="del" scale="1.5" style="margin-top:-2px; float:left; padding-top:1px"></icon><span>删除</span></el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 编辑Form -->
    <el-dialog title="编辑" :visible.sync="dialogFormEditVisible">
      <el-form :model="formEdit" :rules="formEditRules" ref="formEdit">
        <el-row>
        <el-col :span="12">
          <el-form-item label="域名" :label-width="formLabelWidth" size="small" prop="domain">
            <el-input v-model="formEdit.domain" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="IP地址" :label-width="formLabelWidth" size="small" prop="legal_ip">
            <el-input v-model="formEdit.legal_ip" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="cancelForm('formEdit')" size="small">取 消</el-button>
        <el-button type="primary" @click="submitFormEdit('formEdit')" size="small">确 定</el-button>
      </div>
    </el-dialog>

    <div class="pagination" style="float: right; margin-top:10px">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        layout="total, sizes, prev, pager, next, jumper"
        :page-sizes="[5, 10, 20, 50]"
        :page-size="pageSize"
        :total="data.length">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import { restful_path } from '../util.js'
  //Loopback:1 Interface:0
  function isValidIP(ip,type) {
    var reg =  /(^0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])\.(0|([1-9]\d{0,1})|1\d\d|2[0-4]\d|25[0-5])$/;
    return reg.test(ip);
  }

  export default {
    data() {
/*       var ipAddressAddValidator = (rule, value, callback) => {
        if(!value){
          return callback(new Error('IP地址不能为空'));
        }
        setTimeout(() => {
          if(!isValidIP(value, this.formAdd.type)){
            callback(new Error("IP地址不符合要求"));
          } else {
            callback();
          }
        }, 200);
      };
*/
      var ipAddressEditValidator = (rule, value, callback) => {
        if(!value){
          return callback(new Error('IP地址不能为空'));
        }
        setTimeout(() => {
          if(!isValidIP(value, this.formEdit.type)){
            callback(new Error("IP地址不符合要求"));
          } else {
            callback();
          }
        }, 100);
      };

      return {
        data: [],
        currentPage:1,
        pageSize:10,
/*        select_city: [],
        select_isOccupied: [],*/
        dialogFormVisible: false,
        dialogFormEditVisible: false,
        dialogFormUploadVisible: false,
        uploadDataUrl: restful_path + '/api/upload/key-domain',

        formFilter: {
          input_domain: ''
        },

        formAdd: {
          ipAddress: '',
          city: '',
          isOccupied:'',
          type:''
        },
        formEdit: {
          domain: '',
          legal_ip: ''
        },

        formEditRules:{
          domain:[{
            required: true,
            message: '请输入域名',
            trigger: 'blur'
          }],
          legal_ip:[{
            validator: ipAddressEditValidator,
            trigger: 'blur'
          }]
        },

          /*
          type:[{
            required: true,
            message: '请选择地址类型',
            trigger: 'blur'
          }],
          isOccupied:[{
            required: true,
            message: '请选择是否占用',
            trigger: 'blur'
          }],
          ipAddress:[{
            validator: ipAddressEditValidator,
            trigger: 'blur'
          }]
        }, */

        formLabelWidth: '80px',
        fileList: []
        //loading: true
      }
    },
    created() {
      this.showData();
    },
    methods: {

      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      showData() {
        this.$http.get(restful_path + '/api/dns/get-all-key-domain')
        .then(response => {
          if (response.data.status){
            this.data = response.data.data;
          }
        }).catch(error => {
          console.log(error);
        });
      },

      DataFilter() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-single-key-domain',
          data: {
            'domain': this.formFilter.select_domain
          }
        }).then(response => {
          if (response.data.status){
            this.data = response.data.data;
          }
        }).catch(error => {
          console.log(error);
        });
      },

/*       resetSearch(formName){
        this.$refs[formName].resetFields();
      },

      submitFormAdd(formName) {
        this.$refs[formName].validate((valid) => {
          if(valid){
            this.$http({
              method: 'post',
              url: 'http://127.0.0.1:5000/ipManage',
              data: {
                'action': 1,
                'city': this.formAdd.city,
                'ipAddress': this.formAdd.ipAddress,
                'isOccupied': this.formAdd.isOccupied,
                'type': this.formAdd.type
              }
            }).then(response => { console.log(response); }).catch(error => {
              console.log(error);
            });
            this.dialogFormVisible = false;
            this.$refs[formName].resetFields();
            setTimeout(() =>{
              this.$http.get('http://127.0.0.1:5000/ipManage')
                .then(response => {
                  this.data = response.data
                })
                .catch(error => {
                  console.log(error);
                })
            }, 100)
          }
        });
      },

      cancelForm(formName){
        this.dialogFormVisible = false;
        this.$refs[formName].resetFields();
      },
*/

      handleEdit(index, row) {
        this.dialogFormEditVisible = true;
        this.formEdit = Object.assign({}, row);
      },

      submitFormEdit(formName) {
        this.$refs[formName].validate((valid) => { if(valid) {
          let para = Object.assign({}, this.formEdit);
          this.$http({
              method: 'post',
              url: restful_path + '/api/dns/edit-select-domain/' + para.id,
              data: {
                'domain': para.domain,
                'legal_ip': para.legal_ip
              }
            }).then(response => { 
              if(response.data.msg) {
                this.$message({
                  type: 'success',
                  message: '修改成功!'
                });
              } else {
                this.$message({
                  type: 'danger',
                  message: '修改失败!'
                });
              }
             }).catch(error => {
              console.log(error);
            });
            this.dialogFormEditVisible = false;
            this.$refs[formName].resetFields();
            setTimeout(() =>{
              this.$http.get(restful_path + '/api/dns/get-all-key-domain')
                .then(response => {
                  this.data = response.data.data
                })
                .catch(error => {
                  console.log(error);
                })
            }, 100)
          }
        });
      },

      handleDelete(row) {
        this.$confirm('是否将该域名删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http({
            method: 'post',
            url: restful_path + '/api/dns/delete-select-domain',
            data: {
              'id': row['id']
            }
          }).then((response) => {
            if(response.data.msg){
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              setTimeout(() =>{
                this.$http.get(restful_path + '/api/dns/get-all-key-domain')
                  .then(response => {
                    if(response.data.msg) {
                      this.data = response.data.data
                    }
                  })
                  .catch(error => {})
              }, 100)
            }
          }).catch(error => {});
        }).catch(() => {});
      },
      /*
      handleDownload() {
        require.ensure([], () => {
          const { export_json_to_excel } = require('@/vendor/Export2Excel');
          const tHeader = ['地市', 'IP地址', '是否占用'];
          const filterVal = ['city', 'ipAddress', 'isOccupied'];
          const list = this.data;
          const data = this.formatJson(filterVal, list);
          export_json_to_excel(tHeader, data, '列表excel');
          })
      },
      formatJson(filterVal, jsonData) {
        return jsonData.map(v => filterVal.map(j => v[j]))
      },*/
      submitUpload() {
        this.$refs.upload.submit();
      },
      clearUploaded(){
        this.$refs.upload.clearFiles();
      },
      successUpload(response, file, fileList) {
        //console.log(response);
        if(response.status) {
          this.$message({
            type: 'success',
            message: '导入成功!'
          });
          setTimeout(() =>{
            this.$http.get(restful_path + '/api/dns/get-all-key-domain')
              .then(response => {
                if(response.data.msg) {
                  this.data = response.data.data
                }
              })
              .catch(error => {})
          }, 100)
        } else {
          this.$message({
            type: 'error',
            message: '导入失败!' + response.msg
          });
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .handle-box{
    margin-top: 20px;
    text-align: center
  }
  .handle-select-input-domain {
    width: 235px;
  }
</style>
