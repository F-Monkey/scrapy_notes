package indi.monkey.web.bean.vo;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class Response<T> {
	private int status;
	private String msg;
	private T data;
	private Throwable exception;
	private int costTime;
	
	@SuppressWarnings("unchecked")
	public static <T> Response<T> createResp(int status,String msg, T data, Exception exception) {
		return (Response<T>) Response.builder().status(status).msg(msg).data(data).exception(exception)
				.build();
	}

	public static <T> Response<T> createSuccessResp(T data) {
		return createResp(200, null ,data, null);
	}

	public static <T> Response<T> createErrorResp(int costTime, String msg, Exception exception) {
		return createResp(400, msg, null, exception);
	}
}
