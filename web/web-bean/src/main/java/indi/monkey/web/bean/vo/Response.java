package indi.monkey.web.bean.vo;

import lombok.Data;

@Data
public class Response<T> {
	private String status;
	private String msg;
	private T data;
	private Throwable exception;
	private int costTime;
}
